import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import { Layout } from 'antd';

import NewBlog from './pages/NewBlog';

import logo from './logo.svg';
import './App.scss';

const { Header, Footer, Sider, Content } = Layout;

function App() {
  return (
    <Router>
    <div className="App">
      <header id="header">header</header>
      <div id="main">
        <aside id="aside">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/new">new</Link></li>
          </ul>
        </aside>
        <div id="content">

    <Switch>
      <Route path="/new">
        <NewBlog />
      </Route>
      <Route path="/">
        <Home />
      </Route>
    </Switch>
    </div>
      </div>
      <div id="footer">footer</div>
    </div>
    </Router>
  );
}

function Home() {
  return (
    <div className="home">Home1</div>
  )
}

export default App;
