import React from "react";
import "./About.css"

const About = (props) =>{
    console.log(props);
    return (
        <div className="about__container">
            <span>
                "Everyone has a plan until they get punched in the face"
            </span>
        <span>- Mike Tyson, Motherfuckin' Legend</span>
        </div>
    )
}

export default About;