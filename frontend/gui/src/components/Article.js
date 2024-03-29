import React from "react";
import { List, Avatar, Icon } from "antd";

const IconText = ({ type, text }) => (
  <span>
    <Icon type={type} style={{ marginRight: 8 }} />
    {text}
  </span>
);
const Article = props => {
  return (
    <div>
      <h>hiiiiii</h>
      <List
        itemLayout="vertical"
        size="large"
        pagination={{
          onChange: page => {
            console.log(page);
          },
          pageSize: 3
        }}
        dataSource={props.data}
        renderItem={item => (
          <List.Item
            key={item.title}
            actions={[
              <IconText type="star-o" text="156" key="list-vertical-star-o" />,
              <IconText type="like-o" text="156" key="list-vertical-like-o" />,
              <IconText type="message" text="2" key="list-vertical-message" />
            ]}
            extra={<img width={272} alt="logo" src={item.image} />}
          >
            <List.Item.Meta
              avatar={<Avatar src={item.avatar} />}
              title={<a href={`/${item.slug}`}>{item.title}</a>}
              description={item.price}
            />
            {item.content}
          </List.Item>
        )}
      />
    </div>
  );
};
export default Article;
