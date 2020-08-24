import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import { Button } from 'antd';

import hljs from 'highlight.js';
import 'highlight.js/styles/default.css';

import { httpGet, httpDelete } from '../../helper/request.js';

import './index.sass';

// function ArticleItems (props) {
//   const items = props.articles.map(item =>
//   )
//   return (
//     <div>{items}</div>
//   )
// }


export default function Home() {
  const [articles, setArticle] = useState([]);

  async function fetchData() {
    const res = await httpGet('/article/list/');
    setArticle(res.articles);
    document.querySelectorAll("pre code").forEach(block => {
      try{hljs.highlightBlock(block);}
      catch(e){console.log(e);}
    });
  }
  useEffect(() => {
    fetchData();
  }, [])

  async function delArticle(id) {
    const res = httpDelete(`/article/del/${id}/`);
    fetchData();
  }

  const items = articles.map(item =>
    <div key={item._id.$oid}>
      <Link to={`/detail/${item._id.$oid}` }>{item.title}</Link>
      <div dangerouslySetInnerHTML = {{ __html:item.content }}></div>
      <Button type="primary" danger onClick={() => delArticle(item._id.$oid)}>删除</Button>
    </div>
  )

  return (
    <div className="Home">
      <div id="main">
        <aside id="aside">
          <ul>
            <li>123123</li>
            <li>123123</li>
            <li>123123</li>
            <li>123123</li>
          </ul>
        </aside>
        <div id="content">{ items }</div>
      </div>
    </div>
  );
}
