import React, { Component, createRef, useRef } from 'react';
import { InputGroup, FormControl, Row, Col, Table, Button, Form, Modal, Alert, } from 'react-bootstrap';
import { sendQuestion, fetchConverstaion, sendReport } from '../../services/ChatService';
import ConversationEntry from '../../components/ConversationEntry';
import * as XLSX from 'xlsx';

class Conversation extends Component {
  constructor(props) {
    document.title = 'Nueva Conversación';
    super(props);
    this.state = {
      question: '',
      message: '',
      name: 'Nueva conversación',
      messageClass: '',
      conversationId: window.location.href.split('/').pop(),
      conversationEntries : []
    };
    this.questionInputRef = React.createRef();
    this.nameInputRef = React.createRef();
    this.emailInputRef = React.createRef();
  }

  componentDidMount() {
    // TODO: load previous messages from mongodb
    const { conversationId } = this.state;
    fetchConverstaion(conversationId)
      .then(responseData => {
        console.log(responseData);
      })
      .catch(error => {
        console.error(error);
        this.setState({ 
          message: 'Ocurrió un error al traer la conversación',
          messageClass: 'text-danger' 
        });
        setTimeout(() => {
          this.setState({ 
            message: '', 
            messageClass: '' 
          });
        }, 5000);
        setTimeout(() => {
          this.setState({ 
            disabled: false, 
          });
        }, 1500);
      });
  }

  sendMessageClick = () => {
    console.log('sendmessageclik');
    const { question, messages, pagination, conversationId, name, conversationEntries } = this.state;
    const conversationName = name == 'Nueva conversación' ? question : name;
    sendQuestion(question, conversationId, conversationName)
      .then(responseData => {
        console.log('response');
        const newConversationEntryRef = createRef();
        console.log('1 +++++++++++++++++++++++++++++++++');
        const newConversationEntry = (<ConversationEntry 
          ref={newConversationEntryRef} 
          key={conversationEntries.length} 
          columns={responseData.data.columns}
          resultSet={responseData.data.result_set}
          pagination={( responseData.data.result_set.length > 10 ? 
            { ...pagination, show: true, numberPages: Math.ceil(responseData.data.result_set.length / 10) } : 
            { ...pagination, show: false } 
          )}
        />);
        console.log('2 +++++++++++++++++++++++++++++++++');
        console.log(newConversationEntry);
        console.log(newConversationEntryRef);
        newConversationEntry.setRows();

        this.setState((prevState) => ({
          conversationEntries: [...prevState.conversationEntries, { ref: newConversationEntryRef, component: newConversationEntry }],
        }, () => {
          console.log('3 +++++++++++++++++++++++++++++++++');
          const lastEntryRef = this.state.conversationEntries[this.state.conversationEntries.length - 1].ref;
          if (lastEntryRef.current) {
            lastEntryRef.current.setRows();
          }
        }));
      })
      .catch(error => {
        console.error(error);
        this.setState({ 
          message: 'Ocurrió un error al validar el usuario',
          messageClass: 'text-danger' 
        });
        setTimeout(() => {
          this.setState({ 
            message: '', 
            messageClass: '' 
          });
        }, 5000);
        setTimeout(() => {
          this.setState({ 
            disabled: false, 
          });
        }, 1500);
      });
  }

  updateNameClick = () => {
    const { name } = this.state;
    console.log(name);
  }

  render() {
    const { 
      conversationEntries,
      question,
      name, 
    } = this.state;
    //this.questionInputRef.current.focus();

    return (
      <>
        {/* form name */}
        <Row>
          <Col>
            <InputGroup className="mb-3">
              <InputGroup.Text>Nombre de la Conversación</InputGroup.Text>
              <FormControl
                placeholder="Cuál es su pregunta?"
                aria-label="Cuál es su pregunta?"
                aria-describedby="button-send"
                value={this.state.name}
                onChange={(e) => this.setState({ name: e.target.value })}
                ref={this.nameInputRef}
              />
              <Button variant="success" id="button-send" onClick={this.updateNameClick} style={{ width: '120px' }} >
                <i className="fa fa-check" aria-hidden="true" style={{marginRight:'5px'}}></i>Guardar
              </Button>
            </InputGroup>
          </Col>
        </Row>
        {/* answers */}
        {conversationEntries.map(({ component }) => component)}
        {/* form question */}
        <Row>
          <Col>
            <InputGroup className="mb-3">
              <FormControl
                placeholder="Cuál es su pregunta?"
                aria-label="Cuál es su pregunta?"
                aria-describedby="button-send"
                value={this.state.question}
                onChange={(e) => this.setState({ question: e.target.value })}
                ref={this.questionInputRef}
              />
              <Button variant="primary" id="button-send" onClick={this.sendMessageClick} style={{ width: '120px' }} >
                <i className="fa fa-paper-plane-o" aria-hidden="true" style={{marginRight:'5px'}}></i>Enviar
              </Button>
            </InputGroup>
          </Col>
        </Row>
      </>
    );
  }
}

export default Conversation;