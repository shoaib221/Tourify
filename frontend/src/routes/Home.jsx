import React, { useContext, useEffect, useState } from 'react';
import { useTheme } from '../lib/Theme/Theme';
import '../lib/animation/animation1.css'
import { Banner, About, Skill, Project, Achievement, Experience } from './compo.jsx'
import { IoMenu } from "react-icons/io5";



export const Home = () => {

    const { ThemeChoice, ThemeButton2 } = useTheme()

    const [board, setBoard] = useState("intro")
    const [sideMenu, setSideMenu] = useState(false)

    const [scrolled, setScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setScrolled(window.scrollY);
        };

        window.addEventListener("scroll", handleScroll);

        return () => window.removeEventListener("scroll", handleScroll);
    }, []);


    return (
        <div className='flex flex-col  grow relative  w-full pt-12' >
            
            { scrolled }
            <div className="w-full h-80 bg-center bg-cover" style={{ backgroundImage: 'url(https://res.cloudinary.com/deqscvjss/image/upload/logo_tkmvq2.png)' }}  ></div>
            { scrolled }
            <div className="w-full h-200" ></div>
            { scrolled }
            <div className="w-full h-200" ></div>
            { scrolled }
            <div className="w-full h-200" ></div>
            { scrolled }
            <div className="w-full h-200" ></div>
            { scrolled }
            <div className="w-full h-200" ></div>
            { scrolled }
        </div>
    );
};



// Home Page
// Banner: A hero section with a title, description, and a "Search Scholarship" button.
// Top Scholarships (Dynamic): A section displaying the top 6 scholarships (e.g., those
// with the lowest application fees or most recent post date). Each card must have a
// "View Details" button.
// Animation: You must implement animation on the Home page using framer-motion.
// Two Extra Sections: Add two extra static sections. For example:
// 1. A "Success Stories" or "Testimonials" section.
// 2. A "Contact Us" or "F.A.Q" section.
