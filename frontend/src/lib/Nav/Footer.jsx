import React from 'react';
import { RiTwitterXFill } from "react-icons/ri";
import { FaLinkedin, FaFacebook } from "react-icons/fa";
import { TbBrandStocktwits } from "react-icons/tb";
import { Logo } from './Nav';


const SubFooter = () => {

    return (
        <div className='grid grid-cols-1 lg:grid-cols-3 gap-2 justify-evenly' >

            <div>
                <div>Support</div>
                <div>Help Center</div>
                <div>Get help with a safety issue</div>
                <div>AirCover</div>
                <div>Travel insurance</div>
                <div>Anti-discrimination</div>
                <div>Disability support</div>
                <div>Cancellation options</div>
                <div>Report neighborhood concern</div>
            </div>

            <div>
                <div>Hosting</div>
                <div>Airbnb your home</div>
                <div>Airbnb your experience</div>
                <div>Airbnb your service</div>
                <div>AirCover for Hosts</div>
                <div>Hosting resources</div>
                <div>Community forum</div>
                <div>Hosting responsibly</div>
                <div>Airbnb-friendly apartments</div>
                <div>Join a free hosting class</div>
                <div>Find a co‑host</div>
                <div>Refer a host</div>
            </div>

            <div>
                <div>Airbnb</div>
                <div>2026 Summer Release</div>
                <div>Newsroom</div>
                <div>Careers</div>
                <div>Investors</div>
                <div>Gift cards</div>
                <div>Airbnb.org emergency stays</div>
            </div>

        </div>
    )
}


export const Footer = () => {

    return (
        <div id='footer' className='px-8' >
            <div>Inspiration for future getaways</div>

            <div>



            </div>

            <div>

            </div>

            <SubFooter />

            <div className='flex flex-col lg:flex-row gap-2 justify-between' >

            </div>

        </div>
    );
};


// <div style={{ display: 'flex', justifyContent: 'space-between' }} >
//                 <Logo />

//                 <div>
//                     <div>Social Links</div>
//                     <div style={{ display: 'flex', gap: '1rem', fontSize: '1.5rem', marginTop: '1rem' }} >
//                         <RiTwitterXFill title='X' onClick={ () => window.open("https://x.com", "_blank") } />
//                         <FaLinkedin title='Linkedin' onClick={ () => window.open( "https://www.linkedin.com/", "_blank" ) } />
//                         <FaFacebook title='Facebook' onClick={ () => window.open( "https://www.facebook.com", "_blank" ) } />
//                     </div>
//                 </div>
//             </div>

//             <div style={{ textAlign: 'center', marginTop: '1rem' }} >
//                 Copyright © 2025 - All right reserved
//             </div>

