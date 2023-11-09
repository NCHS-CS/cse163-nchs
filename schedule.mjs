import fs from 'fs';
import yaml from 'js-yaml';

// This stuff is terrible and should be in a mini library, sorry.
function text(value) {
  return { type: 'text', value };
}
function link(value, url) {
  return { type: 'link', url, children: [text(value)] };
}
function tableCell(value, opts) {
  const children = typeof value === 'string' ? [text(value)] : value;
  return { type: 'tableCell', children, ...opts };
}
function span(value, style) {
  const children = typeof value === 'string' ? [text(value)] : value;
  return { type: 'span', children, style };
}
function tableRow(cells) {
  return { type: 'tableRow', children: cells };
}

// We don't have custom css quite yet  :(
const classes = {
  lecture: { background: '#4E66F6', borderRadius: 8, color: 'white', padding: 5 },
  participation: { background: '#7A77B4', borderRadius: 8, color: 'white', padding: 5 },
  lab: { background: '#B83BC0', borderRadius: 8, color: 'white', padding: 5 },
  homework: { background: '#D43B21', borderRadius: 8, color: 'white', padding: 5 },
};

const scheduleDirective = {
  name: 'schedule',
  doc: 'Schedule directive presents a schedule based on a YAML file',
  // The arg should probably be the YAML file you are loading
  // arg: { type: String },
  options: {
    // size: { type: String },
  },
  run(data) {
    // ## Week 1
    // Aug 24 [Lecture 1]     PDF Document        (note)
    //        [Exercise 1.1]  PDF Document
    const weeks = yaml.load(fs.readFileSync('./schedule.yml').toString());
    const children = weeks.map(({ week, days }) => {
      const renderedDays = days
        .map((day) => {
          const rows = day.items.map(({ type, id, name, href, auxil }) =>
            tableRow([
              tableCell([span(`${type} ${id}`, classes[type.toLowerCase()])]),
              tableCell([link(name, href)]),
              auxil ? tableCell([link(auxil.id, auxil.href)]) : tableCell([]),
            ])
          );
          // Put a header on the first row that spans all of them!
          rows[0].children.unshift(tableCell(day.date, { rowspan: day.items.length }));
          return rows;
        })
        .flat(); // turns this into a flat list of children
      return {
        type: 'card',
        identifier: `week${week}`, // Can link to this and show a preview
        children: [
          {
            type: 'header',
            children: [{ type: 'text', value: `Week ${week}` }],
          },
          { type: 'table', children: renderedDays },
        ],
      };
    });

    return children.flat();
  },
};

const plugin = { name: 'Schedule Directive', directives: [scheduleDirective] };

export default plugin;
