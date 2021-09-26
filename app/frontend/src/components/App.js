import React from "react";
import {render} from "react-dom";

export default function App(props) {
    return (
        <h1>Welcome to React</h1>
    )
}

const appDiv = document.getElementById("app")
render(<App/>, appDiv)