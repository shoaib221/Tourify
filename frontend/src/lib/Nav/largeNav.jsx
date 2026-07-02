import { useEffect, useState } from "react"

export const Logo = () => {

    return (
        <div className='h-[3rem] text-(--color4) flex gap-2 items-center' >
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

    return (
        <div className='grow flex flex-col items-center bg-(--color1)' >


            <div className='flex gap-2 p-2' >
                <div>Home</div>
                <div>Experiences</div>
                <div>Services</div>
            </div>

            <div className='flex gap-2 p-2 border w-full max-w-150 justify-evenly' >
                <div>When</div>
                <div>Where</div>
                <div>Type of Service</div>

            </div>

        </div>
    )
}




export const LargeNav = () => {
    const [scrolled, setScrolled] = useState(0);
    const [showLarger, setShowLarger] = useState(false);

    useEffect(() => {
        const scroll = () => {
            setScrolled(window.scrollY);
        };

        window.addEventListener("scroll", scroll);

        return () => window.removeEventListener("scroll", scroll);
    }, []);



    return (
        <>
            { showLarger && (
                <div className='fixed inset-0 bg-black/50 z-20' onClick={() => setShowLarger( false ) } >

                </div>
            )}
            <div className={`nav-1 bg-(--color1) z-30 hidden lg:flex gap-2 p-2 justify-between ${scrolled > 20 ? 'border' : ''}`} onCLick={() => alert( 'hello 1')} >
                <Logo />

                {
                    scrolled > 20 && !showLarger ? <SubNav setShowLarger={setShowLarger} /> : <SubNav2 />
                }

                <div className='flex gap-2 p-2' >
                    <div> G </div>
                    <div> Menu </div>
                </div>
            </div>
        </>
    )
}
