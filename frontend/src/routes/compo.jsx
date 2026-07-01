import '../lib/Theme/Theme.css';
import '../lib/Box/box1.css';
import { skills, projects, achievements, contacts, education } from '../data/skills';
import { Box12, Box13, Box14, Box15, Box16, Box17 } from '../lib/Box/box1.jsx';
import { FaGlobe } from "react-icons/fa";


export const Banner = () => {
	return (
		<div id='banner' className='mb-8 lg:mb-0 w-full lg:w-80 lg:min-w-80 flex flex-col justify-start gap-2 items-center lg:sticky lg:top-12 self-start' >
			<div className='h-50 w-50 rounded-full bg-contain bg-top bg-no-repeat' style={{ backgroundImage: `url(/shoaib2.jpg)` }} ></div>
			<div className='header-1' >Md Shoaib Tasrif Emon</div>
			<div className='font-bold text-center' >Software Developer</div>
			
		</div>
	)
}


export const About = () => {
	return (
		<div  className='w-full gap-4 p-4' >
			<div className='header-1' >About Me</div>
			<div className='text-justify' >
				I am a software development enthusiast who is passionate about building modern softwares and solving algorithmic problems with efficiency. 
				I have experience in web development & competitive programming.
			</div>

			<div className='h-8'></div>

			<div className='header-1' >Academic History</div>


			<div className='w-full flex flex-col gap-4 items-center' >
				{education.map((skill, index) => <Box17 key={index} data={skill} />)}
			</div>


			<div className='h-8'></div>


			<div className='header-1' >Trace Me</div>
			<div className='w-full flex flex-col gap-4 items-center' >
				{contacts.map((skill, index) => <Box16 key={index} data={skill} />)}
			</div>
		</div>
	)
}


export const Skill = () => {

	return (
		<div  className='w-full p-4' >
			<div className='header-1' >Programming Skills</div>
			<div className='w-full flex flex-col items-center gap-4 p-4' >
				{skills.map((skill, index) => <Box12 key={index} job={skill} />)}
			</div>
		</div>
	)
}


export const Project = () => {

	return (
		<div  className='w-full gap-4 p-4' >
			<div className='header-1' >Software Projects</div>

			<div className='w-full flex flex-col gap-4' >
				{projects.map((skill, index) => <Box13 key={index} job={skill} />)}
			</div>
		</div>
	)
}


export const Achievement = () => {

	return (
		<div  className='w-full gap-4 p-4 grow' >
			<div className='header-1' >Honors & Certifications</div>

			<div className='w-full flex flex-col gap-4' >
				{achievements.map((skill, index) =>   <Box15 key={index} job={skill} /> )}
			</div>
		</div>
	)
}


export const Experience = () => {

	return (
		<div  className='w-full gap-4 p-4' >
			<div className='header-1' >Professional Experiences</div>
			<div className='text-center' >No experience yet</div>
		</div>
	)
}


