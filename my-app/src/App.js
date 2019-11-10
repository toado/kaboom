import React from 'react';
import Title from './components/Title'
import Search from './components/Search'
import Select from './components/Select'
import './App.css';

export default class landingPage extends React.Component {
  render() {
    return(
      <div className = "main">
        <Title />
        <Search />
        <br>
        </br>
        <Select />

      </div>
    )
  }
}