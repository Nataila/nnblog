import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import { Layout } from 'antd';

import Home from './pages/Home';
import Admin from './pages/Admin';
import ArticleDetail from './pages/ArticleDetail';

import './App.scss';

function App() {
  return (
    <Router>
    <div className="App">
      <header id="header">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/admin">admin</Link></li>
            <li><Link to="/admin/new/">new</Link></li>
          </ul>
      </header>
    <Switch>
      <Route path="/admin">
        <Admin />
      </Route>
      <Route path="/detail/:id">
        <ArticleDetail />
      </Route>
      <Route path="/">
        <Home />
      </Route>
    </Switch>
    <div id="footer">footer</div>
    </div>
    </Router>
  );
}

export default App;
