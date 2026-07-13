import { useEffect, useState } from "react";
import { IoIosMenu } from "react-icons/io";
import './largeNav.css';
import { RxCross1 } from "react-icons/rx";
import { useNavigate } from "react-router-dom";


export const Logo = () => {
    const navigate = useNavigate();

    return (
        <div className='h-[3rem] text-(--color4) flex gap-2 items-center' onClick={ () => navigate('/') } >
            <div className='h-6 w-6 bg-cover bg-center' style={{ backgroundImage: 'url(/static/logo.png)' }} ></div>
            <div className='cen-ver text-(--color4) font-bold' >tourify</div>
        </div>
    )
}

export const SubNav = ({ setShowLarger }) => {

    return (
        <div className='flex gap-2 p-2' onClick={() => setShowLarger(true)} >
            <div>Anywhere</div>
            <div>Anytime</div>
            <div>Add Services</div>
        </div>
    )
}

const SubNav2 = ({ title, path }) => {
    const navigate = useNavigate();

    return (
        <div className='grow flex flex-col items-center bg-(--color1)' >


            <div className='flex gap-2 p-2' >
                <div onClick={() => navigate('/homes')} >Homes</div>
                <div onClick={() => navigate('/experiences')} >Experiences</div>
                <div onClick={() => navigate('/services')} >Services</div>
            </div>

            <div className='flex gap-2 p-2 border w-full max-w-150 justify-evenly' >
                <div>When</div>
                <div>Where</div>
                <div>Type of Service</div>

            </div>

        </div>
    )
}



const MenuBar = ( { showMenu, setShowMenu } ) => {
    return (
        <>
            { showMenu && (
                <div className='fixed inset-0 bg-black/50 z-40' onClick={() => setShowMenu(false)} >
                    {/* Shadow */}
                </div>
            )}

            <div className={`${ showMenu ? 'selected' : '' } menu-bar`} >
                <RxCross1 className='text-xl cursor-pointer m-2' onClick={() => setShowMenu(false)} />

            </div>
        </>

    )
}


export const LargeNav = () => {
    const [scrolled, setScrolled] = useState(0);
    const [showLarger, setShowLarger] = useState(false);
    const [showMenu, setShowMenu] = useState(false);

    useEffect(() => {
        const scroll = () => {
            setScrolled(window.scrollY);
            if (window.scrollY < 20) {
                setShowLarger(false);
            }
        };

        window.addEventListener("scroll", scroll);

        return () => window.removeEventListener("scroll", scroll);
    }, []);

    useEffect(() => {
        if (showMenu) {
            document.body.style.overflow = "hidden";
        } else {
            document.body.style.overflow = "auto";
        }

    }, [showMenu]);



    return (
        <>
            {showLarger && scrolled > 20 && (
                <div className='fixed inset-0 bg-black/50 z-20' onClick={() => setShowLarger(false)} >
                    {/* Shadow */}
                </div>
            )}
            <div className={`nav-1 bg-(--color1) z-30 hidden lg:flex gap-2 p-2 justify-between ${scrolled > 20 ? 'border' : ''}`} onCLick={() => alert('hello 1')} >
                <Logo />

                {
                    scrolled > 20 && !showLarger ? <SubNav setShowLarger={setShowLarger} /> : <SubNav2 />
                }



                <IoIosMenu onClick={() => setShowMenu(true)}  className='text-xl cursor-pointer' />

                <MenuBar showMenu={showMenu} setShowMenu={setShowMenu} />

            </div>
        </>
    )
}
