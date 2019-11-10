import React from 'react';
import Title from './components/Title'
import Search from './components/Search'
import Select from './components/Select'
import Generate from './components/Generate'

import './App.css';

console.log(window.location.search)

export default class landingPage extends React.Component {
  render() {
    return(
      <div className = "main">
        <Title />
        <br>
        </br>
        <Search />
        <br>
        </br>
        <Select />
        <br>
        </br>
        <Generate />
      </div>
    )
  }
}