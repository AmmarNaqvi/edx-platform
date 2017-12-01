import React from 'react';

export class HelloWorld extends React.Component {
  render() {
    return <div>hello world {this.props.foo}</div>;
  }
}
