import React from "react";
import "../assets/css/navbar.css"

const NavBar = (props) => {
    return (
        <div id="navbar" className="container">
            <div id="title">
                <h2 style={{marginTop: "20px", marginBottom: "0px"}}>
                    Vietnamese Open-domain question answering for COVID-19 topic
                </h2>
            </div>
        </div>
    )
}

export default NavBar;