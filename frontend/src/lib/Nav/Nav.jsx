
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


export const Logo = () => {

    return (
        <div className='h-[3rem] text-(--color4) flex gap-2 items-center' >
            <div className='h-6 w-6 bg-cover bg-center' style={{ backgroundImage: 'url(/static/logo.png)' }} ></div>
            <div className='cen-ver text-(--color4) font-bold' >tourify</div>
        </div>
    )
}

export const Nav = () => {
    const { ThemeChoice } = useTheme()

    const [down1, setDown1] = useState(true)
    const navigate = useNavigate()
    const [navi, selectNavi] = useState("home")
    const location = useLocation()

    function DownWindow(wind, path) {

        setDown1(wind)
        if (path) navigate(path)

    }

    useEffect(() => {
        //console.log("Location change")
        let path = location.pathname.toLowerCase();
        if (path.includes("all-scholarships")) selectNavi("all-scholarships");
        else if (path.includes("dashboard")) selectNavi("dashboard");
        else if (path.includes("detail")) selectNavi("details");
        else selectNavi("home");
    }, [location?.pathname])




    useEffect(() => {

        function handleResize() {

            if (window.innerWidth > 768) {
                setDown1(true)
            }
        }

        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, [])


    return (
        <nav class="bg-white border-b border-gray-200 px-6 py-4">
            <div class="max-w-7xl mx-auto flex items-center justify-between">

                {/* <!-- Logo --> */}
                <div class="flex items-center space-x-2">
                    <svg class="w-8 h-8 text-rose-500" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2c-.8 0-1.5.4-1.9 1.1L3.7 16.2c-.6 1.2.3 2.8 1.7 2.8h13.2c1.4 0 2.3-1.5 1.7-2.8L13.9 3.1C13.5 2.4 12.8 2 12 2z" />
                    </svg>
                    <span class="text-2xl font-bold text-rose-500">Tourify</span>
                </div>

                {/* <!-- Search Bar --> */}
                <div class="hidden md:flex items-center bg-white border border-gray-300 rounded-full shadow-sm hover:shadow-md transition">
                    <button class="px-6 py-3 text-sm font-semibold">
                        Anywhere
                    </button>

                    <div class="w-px h-6 bg-gray-300"></div>

                    <button class="px-6 py-3 text-sm font-semibold">
                        Any week
                    </button>

                    <div class="w-px h-6 bg-gray-300"></div>

                    <button class="px-6 py-3 text-sm text-gray-500">
                        Add guests
                    </button>

                    <button class="m-2 bg-rose-500 p-2 rounded-full text-white hover:bg-rose-600">
                        🔍
                    </button>
                </div>

                {/* <!-- Right Side --> */}
                <div class="flex items-center space-x-4">

                    <button class="hidden md:block text-sm font-semibold hover:bg-gray-100 px-4 py-2 rounded-full">
                        Become a host
                    </button>

                    <button class="p-2 hover:bg-gray-100 rounded-full">
                        🌐
                    </button>

                    <button class="flex items-center space-x-3 border border-gray-300 rounded-full px-3 py-2 hover:shadow-md">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h16" />
                        </svg>

                        <div class="w-8 h-8 rounded-full bg-gray-400 flex items-center justify-center text-white">
                            👤
                        </div>
                    </button>

                </div>

            </div>
        </nav>
    )



    // return (
    //     <nav id='top' className='flex min-h-[3rem] justify-between px-4 items-center fixed top-0 left-0 right-0 bg-(--color1) z-30' >
    //         <Logo />

    //         {/* small screen */}
    //         <div className={`${down1 ? "hidden" : "flex"} absolute z-2 h-[100%] w-[100%] bg-[var(--color1)]  flex-col items-center top-0 left-0 p-4 gap-4`}  >
    //             <div onClick={() => DownWindow(true, "/")} className={`class-1 ${navi === "home" && "active-navi"}`}  >Home</div>
    //             <div onClick={() => DownWindow(true, "/all-scholarships")} className={`class-1 ${navi === "all-scholarships" && "active-navi"}`} >Scholarships</div>
    //         </div>

    //         {/* large screen */}
    //         <div className='hidden lg:flex text-[0.9rem] gap-4 items-center' >
    //             <div onClick={() => DownWindow(true, "/")} className={`class-1 ${navi === "home" && "active-navi"}`}  >Home</div>
    //             <div onClick={() => DownWindow(true, "/all-scholarships")} className={`class-1 ${navi === "all-scholarships" && "active-navi"}`} >Scholarships</div>
    //         </div>

    //         <div className='block lg:hidden text-[0.9rem] gap-4 items-center' >
    //             Menu
    //         </div>

    //         <Profile />

    //     </nav>
    // );
};




