import './App.css';
import Navbar from './Components/Navbar';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Home from './Pages/Home';
import Calendar from './Pages/Calendar';
import ChatBot from './Pages/ChatBot';

function App() {
  return (
    <>
        <Router>
          <Navbar />
          <Switch>
            <Route path='/' exact component={Home} />
            <Route path='/calendar' component={Calendar} />
            <Route path='/chatbot' component={ChatBot} />
            </Switch>
        </Router>

    </>
  );
}

export default App;
