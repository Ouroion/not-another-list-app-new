import React from 'react';
import Lists from '../Lists/Lists';
import Tasks from '../Tasks/Tasks';

export default function Dashboard() {
  return(
    <div>
      <h2>Lists</h2>
      <Lists></Lists>
      <h2>Tasks of List</h2>
      <Tasks></Tasks>
    </div>
  );
}