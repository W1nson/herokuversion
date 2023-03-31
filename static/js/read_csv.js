// Get the container element for the table
const container = document.getElementById('table-container');

// Parse the CSV data and create an HTML table
function renderCSVToTable(csvData) {
  // Split the CSV data into lines
  const lines = csvData.split('\n');

  // Create a new table element
  const table = document.createElement('table');

  // Iterate over the lines and create a new row for each line
  lines.forEach(line => {
    const row = document.createElement('tr');

    // Split the line into an array of values
    const values = line.split(',');

    // Iterate over the values and create a new cell for each value
    values.forEach(value => {
      const cell = document.createElement('td');
      cell.textContent = value;
      row.appendChild(cell);
    });

    // Add the row to the table
    table.appendChild(row);
  });

  // Add the table to the container element
  container.appendChild(table);
}

// Example usage
const csvData = `Name, Age, Country
John Doe, 25, USA
Jane Smith, 30, Canada
Bob Johnson, 45, UK`;

renderCSVToTable(csvData);
