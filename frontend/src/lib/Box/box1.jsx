import React, { useContext, useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import './box1.css';
import '../Buttons/button.css';
import { useNavigate } from 'react-router-dom';
import { IoPerson } from "react-icons/io5";
import { BiCategory } from "react-icons/bi";
import { FaGlobe } from "react-icons/fa";


export const Box11 = ({ job }) => {
    const navigate = useNavigate();

    return (
        <div className='h-[15rem] p-2 box-1' >
            <div className='w-full h-[7rem] bg-cover bg-center' style={{ backgroundImage: `url(${job.coverImage})` }} >  </div>
            <div className='font-bold' >{job.title} </div>
            <div className='text-[.8rem] italic' > {job.summary.substring(0, 80)} ...</div>
            <div className='flex text-[.7rem] justify-between' >
                <div className='flex gap-1 items-center' > <IoPerson /> {job.postedBy} </div>
                <div className='flex gap-1 items-center' > {job.category} <BiCategory /> </div>
            </div>
            <button className='button-1' onClick={() => navigate(`/job-detail/${job._id}`)} >
                View Detail
            </button>
        </div>
    )
}


export const Box12 = ({ job }) => {
    const navigate = useNavigate();

    return (
        <div className='w-full p-2 box-1 flex flex-col' >

            <div className='flex justify-start gap-2 items-center mb-2' >
                <div className='h-6 w-6 p-2  bg-cover bg-center rounded-full' style={{ backgroundImage: `url(${job.photo})` }} ></div>
                <div className='header-2' >{job.name} </div>
            </div>
            
            
            <div className='text-justify' > {job.description} </div>

        </div>
    )
}

export const Box13 = ({ job }) => {
    const navigate = useNavigate();

    return (
        <div className='p-2 box-1 flex flex-col gap-1 justify-between' >
            <div className='flex gap-4 items-center text-(--color4)' >
                <FaGlobe  />
                <div className='header-2'  > {job.name}  </div>
                <div title='Visit Live' onClick={() => window.open(job.live, "_blank", "noopener,noreferrer")} className='button-5' >live</div>
                <button className='button-5' onClick={() => window.open(job.source, "_blank", "noopener,noreferrer")}>
                    source
                </button>
            </div>
            
            <div className='text-justify' > {job.description} </div>

            

        </div>
    )
}


export const Box14 = ({ job }) => {
    return (
        <div className='flex  box-1 flex-col sm:flex-row-reverse p-2 gap-2 w-full max-w-[900px] mx-auto' >

            <div title='Visit Live' onClick={() => window.open(job.live, "_blank", "noopener,noreferrer")}
                className='h-72 sm:h-80 w-full bg-cover bg-top sm:w-[50%] sm:min-w-[50%]' style={{ backgroundImage: `url(${job.photo})` }} ></div>

            <div className='w-full sm:flex-grow flex flex-col items-end justify-center' >
                <div className='font-bold text-lg mb-2' >{job.name} </div>
                <div className='text-[.9rem] italic' > {job.description} </div>

                <button className='button-3 mt-2' onClick={() => window.open(job.source, "_blank", "noopener,noreferrer")}>
                    view
                </button>
            </div>

        </div>
    )
}


export const Box15 = ({ job }) => {
    return (
        <div className='flex  box-1  flex-col p-2 gap-2 w-full' >

            <div className='flex gap-2 items-center' >
                <div className='h-8 w-8 bg-cover bg-center rounded-full' style={{ backgroundImage : `url(${ job.image })` }} > </div>
                <div className='header-2' >{job.name} </div>
                <button className='button-5' onClick={() => window.open(job.source, "_blank", "noopener,noreferrer")}>
                    view
                </button>
            </div>
            
            <div className='text-justify' > {job.description} </div>
        </div>
    )
}


export const Box16 = ( { data } ) => {
    return (
        <div className="box-1 cursor-pointer w-full flex flex-row gap-2 items-center" onClick={ () => window.open( data.link, "_blank", "noopener,noreferrer" ) }>
            <div className='rounded-lg h-6 w-6 p-1 bg-cover bg-center' style={{ backgroundImage: `url(${data.photo})` }} ></div>
            <div className='header-2' >{data.name}</div>
        </div>
    )
}

export const Box17 = ( { data } ) => {
    return (
        <div className="box-1 cursor-pointer w-full flex flex-row gap-2 items-center" onClick={ () => window.open( data.link, "_blank", "noopener,noreferrer" ) }>
            <div className='rounded-lg h-6 w-6 p-1 bg-cover bg-center' style={{ backgroundImage: `url(${data.photo})` }} ></div>
            <div>
                <div className='header-2' style={{ textAlign: 'left' }} >{data.name}</div>
                <div  >{data.name2}</div>
            </div>
            
        </div>
    )
}
