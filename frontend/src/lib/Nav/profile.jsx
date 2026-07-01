import { useEffect, useRef, useState } from "react";
import { useAuthContext } from "../auth/context";
import { Link, useNavigate } from "react-router-dom";




export const Profile = ({ image = "/avatar.jpg", }) => {

    const [open, setOpen] = useState(false);
    const dropdownRef = useRef(null);
    const { user, LogOut, Login } = useAuthContext();
    const navigate = useNavigate();
    

    // Close dropdown when clicking outside
    useEffect(() => {
        const handleClickOutside = (e) => {
            if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
                setOpen(false);
            }
        };
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);


    if(!user) return <button className="button-4" onClick={ () => navigate('/auth') } >Login</button>

    return (
        <div className="relative" ref={dropdownRef}>
            {/* Profile Image */}
            <button
                onClick={() => setOpen(!open)}
                className="w-10 h-10 rounded-full overflow-hidden border-2 border-gray-200 focus:outline-none"
            >
                <img
                    src={user?.photo}
                    alt="Profile"
                    className="w-full h-full object-cover"
                />
            </button>

            {/* Dropdown */}
            {open && (
                <div className="absolute right-0  w-48 bg-(--color4) rounded-lg shadow-lg border z-50">
                    <ul className="py-1 text-sm text-(--color1)">
                        <li>
                            <Link
                                to="/profile"
                                className="block px-4 py-2 hover:opacity-80 cursor-pointer"
                            >
                                Profile
                            </Link>
                        </li>
                        
                        
                        <li>
                            <hr className="my-1" />
                        </li>
                        <li>
                            <button onClick={LogOut}
                                className="w-full text-left px-4 py-2 text-red-600 hover:opacity-80 cursor-pointer"
                            >
                                Logout
                            </button>
                        </li>
                    </ul>
                </div>
            )}
        </div>
    );
};