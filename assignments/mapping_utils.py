import json
import numpy as np

from geopandas.plotting import _plot_polygon_collection


with open("expected_idx.json") as f:
    rural_idx, rural_la_idx, urban_ha_idx, lalowi_idx = json.load(f)


class MockAxes:
    def add_collection(self, *args, **kwargs):
        pass

    def autoscale_view(self, *args, **kwargs):
        pass


def assert_patches_allclose(actual_patches, ax=MockAxes(), num_colors=None, layer=None, **kwargs):
    """Assert that the actual patches match the geometries specified in kwargs and the number of colors."""
    layer_information = ""
    if layer is not None:
        layer_information = f" in layer {layer}"
        if layer == 0:
            layer_information += " which is expected to be the background"
        elif layer > 0:
            layer_information += " which is expected to be the foreground"

    expected_patches = _plot_polygon_collection(ax=ax, **kwargs)
    for expected, actual in zip(expected_patches.get_paths(), actual_patches.get_paths()):
        try:
            np.testing.assert_allclose(expected.vertices, actual.vertices)
        except AssertionError as e:
            e.args = f"wrong selection{layer_information}",
            raise e

    if "color" in kwargs:
        try:
            np.testing.assert_allclose(expected_patches.get_fc(), actual_patches.get_fc())
        except AssertionError as e:
            e.args = f"wrong color{layer_information}",
            raise e
    elif isinstance(num_colors, int):
        num_unique = len(np.unique(actual_patches.get_fc(), axis=0))
        assert num_unique == num_colors, f"expected {num_colors} colors, got {num_unique} colors{layer_information}"