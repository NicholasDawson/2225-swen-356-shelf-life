import { Component } from "react";
import './signup.css'
import logo from './image.png'
class SignUp extends Component {
    constructor(props){
        super(props);
        this.state = {
            //insert here
        }
    }

    render() {
        return (
            <body class="form-cont">
                <img src={logo} alt=""/>
                <main class="form-signin w-100 m-auto">
                <form>
                    <h1 class="h3 mb-3 fw-normal">Sign Up</h1>

                    <div class="form-floating">
                        
                        <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com"></input>
                        <label for="floatingInput">Email address: </label>
                    </div>
                    <div class="form-floating">
                        
                        <input type="password" class="form-control" id="floatingPassword" placeholder="Password"></input>
                        <label for="floatingPassword">Password: </label>
                    </div>
                    <div class="form-floating">
                        
                        <input type="password" class="form-control" id="floatingPasswordC" placeholder="Password"></input>
                        <label for="floatingPasswordC">Confirm Password: </label>
                    </div>
                    <button class="w-100 btn btn-lg btn-primary b_color" type="submit">Sign Up</button>
                </form>
                </main>
            </body>
        )
    }
}
export default SignUp