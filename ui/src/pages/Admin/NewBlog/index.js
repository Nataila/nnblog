/**
* @description
*   + description
# cc @ 2020-08-18 22:13:39
*/

import React, { useState, useEffect } from 'react';

import { Input, Button } from 'antd';
import axios from 'axios';
import Editor from 'react-editor-md';

const NewBlog = () => {
  const [editorInstance, setEditor] = useState()
  const [form, setForm] = useState({})
  function titleChange(e) {
    setForm({title: e.target.value})
  }
  function submit() {
    const content = editorInstance.getHTML()
    const postData = {...form, content}
    axios.post('http://localhost:8000/new/', postData)
      .then(res=> {
        console.log(res);
      })
  }
  return (
      <div>
      <Input placeholder="Basic usage" onChange={titleChange} />
      <Editor config={
        {
          width: '100%',
            markdown: 'editor',
            onload: (editor, func) => {
              setEditor(editor);
            },
        }
      }/>
      <Button onClick={submit} type="primary" htmlType="submit">Submit</Button>
      </div>
  )
};

export default NewBlog;
