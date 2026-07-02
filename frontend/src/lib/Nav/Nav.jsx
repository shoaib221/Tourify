
import React, { useEffect, useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import { FaGithub } from 'react-icons/fa';
import { useNavigate, useLocation } from 'react-router-dom';
import { SignOut } from '../auth/auth';
import './Nav.css';
import { Breaker } from '../miscel/Breaker.jsx';
import { FaGraduationCap } from "react-icons/fa6";
import { useTheme } from '../Theme/Theme.jsx';
import { Profile } from './profile.jsx';
import Navbar from './tmp.jsx';
import { LargeNav } from './largeNav.jsx';


export const Logo = () => {

    return (
        <div className='h-[3rem] text-(--color4) flex gap-2 items-center' >
            <div className='h-6 w-6 bg-cover bg-center' style={{ backgroundImage: 'url(/static/logo.png)' }} ></div>
            <div className='cen-ver text-(--color4) font-bold' >tourify</div>
        </div>
    )
}




const SmallNav = () => {

    return (
        <div className='block lg:hidden nav-1' >Small Nav</div>
    )
}


export const Nav = () => {
    
    return (
        <>
            <LargeNav />
            <SmallNav />
        </>
    )
};




