import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import { Layout, Form, Input, Modal, Button } from 'antd';

import Home from './pages/Home';
import Admin from './pages/Admin';
import ArticleDetail from './pages/ArticleDetail';

import './App.scss';

function App() {
  const [visible, setVisible] = useState(false);

  const layout = {
    labelCol: { span: 8 },
    wrapperCol: { span: 16 }
  };

  const tailLayout = {
    wrapperCol: { offset: 8, span: 16 }
  };

  const onFinish = values => {
    console.log('Success:', values);
  };

  const onFinishFailed = errorInfo => {
    console.log('Failed:', errorInfo);
  };

  function handleCancel() {
    setVisible(false)
  }

  return (
    <Router>
    <Modal
      title="登录"
      visible={visible}
      onCancel={handleCancel}
    >
    <Form
      {...layout}
      name="basic"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[{ required: true, message: 'Please input your username!' }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[{ required: true, message: 'Please input your password!' }]}
      >
        <Input.Password />
      </Form.Item>
    </Form>
    </Modal>
    <div className="App">
      <header id="header">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/admin">admin</Link></li>
            <li><Link to="/admin/new/">new</Link></li>
          </ul>
      <Button type="primary" onClick={() => {setVisible(true)}}>登录</Button>
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
