import { useState, useEffect } from "react";
import {
    Search,
    Globe,
    Menu,
    UserCircle2,
} from "lucide-react";

export default function Navbar() {
    const [expanded, setExpanded] = useState(false);
    const [scrolled, setScrolled] = useState(false);

    useEffect(() => {
        const scroll = () => {
            setScrolled(window.scrollY > 20);
        };

        window.addEventListener("scroll", scroll);

        return () => window.removeEventListener("scroll", scroll);
    }, []);

    return (
        <>
            <nav
                className={`sticky top-0 z-50 bg-white transition-all duration-300
        ${scrolled
                        ? "shadow-md border-b"
                        : "border-b border-gray-200"
                    }`}
            >
                <div className="max-w-7xl mx-auto h-20 flex items-center justify-between px-6">

                    {/* LOGO */}

                    <div className="flex items-center space-x-2 cursor-pointer">

                        <div className="w-9 h-9 rounded-xl bg-rose-500 flex items-center justify-center text-white font-bold">
                            T
                        </div>

                        <span className="hidden md:block text-2xl font-bold text-rose-500">
                            Tourify
                        </span>

                    </div>

                    {/* SEARCH */}

                    <div
                        onClick={() => setExpanded(true)}
                        className={`
            hidden md:flex
            cursor-pointer
            items-center
            rounded-full
            border
            bg-white
            transition-all
            duration-300
            hover:shadow-lg
            ${expanded
                                ? "w-[720px] h-20 px-2"
                                : "w-[370px] h-16 px-3"
                            }
          `}
                    >
                        {!expanded && (
                            <>
                                <div className="flex-1 text-center text-sm font-semibold">
                                    Anywhere
                                </div>

                                <div className="w-px h-6 bg-gray-300"></div>

                                <div className="flex-1 text-center text-sm font-semibold">
                                    Any week
                                </div>

                                <div className="w-px h-6 bg-gray-300"></div>

                                <div className="flex-1 text-center text-sm text-gray-500">
                                    Add guests
                                </div>

                                <button className="w-11 h-11 rounded-full bg-rose-500 flex items-center justify-center text-white">
                                    <Search size={18} />
                                </button>
                            </>
                        )}

                        {expanded && (
                            <div className="grid grid-cols-4 gap-2 w-full">

                                <Field
                                    title="Where"
                                    value="Search destinations"
                                />

                                <Field
                                    title="Check in"
                                    value="Add dates"
                                />

                                <Field
                                    title="Check out"
                                    value="Add dates"
                                />

                                <div className="flex items-center rounded-full hover:bg-gray-100">

                                    <div className="flex-1 px-5">

                                        <p className="text-xs font-bold">
                                            Guests
                                        </p>

                                        <p className="text-sm text-gray-500">
                                            Add guests
                                        </p>

                                    </div>

                                    <button className="mr-2 h-12 w-12 rounded-full bg-rose-500 flex items-center justify-center text-white">
                                        <Search />
                                    </button>

                                </div>

                            </div>
                        )}
                    </div>

                    {/* RIGHT */}

                    <div className="flex items-center space-x-4">

                        <button className="hidden lg:block px-4 py-3 rounded-full hover:bg-gray-100 font-medium">
                            Become a Host
                        </button>

                        <button className="hidden lg:flex h-10 w-10 rounded-full items-center justify-center hover:bg-gray-100">
                            <Globe size={20} />
                        </button>

                        <button className="flex items-center rounded-full border p-2 hover:shadow-md">

                            <Menu size={18} />

                            <UserCircle2
                                size={32}
                                className="ml-3 text-gray-500"
                            />

                        </button>

                    </div>
                </div>

                {/* MOBILE */}

                <div className="md:hidden px-5 pb-4">

                    <button className="w-full rounded-full border h-14 flex items-center px-4 shadow">

                        <Search className="text-gray-600" size={18} />

                        <div className="ml-4">

                            <p className="font-semibold text-left">
                                Where to?
                            </p>

                            <p className="text-xs text-gray-500">
                                Anywhere • Any week • Guests
                            </p>

                        </div>

                    </button>

                </div>

            </nav>

            {/* Overlay */}

            {expanded && (
                <div
                    className="fixed inset-0 bg-black/20 z-40"
                    onClick={() => setExpanded(false)}
                />
            )}
        </>
    );
}

function Field({ title, value }) {
    return (
        <div className="rounded-full px-5 py-4 hover:bg-gray-100">
            <p className="text-xs font-bold">{title}</p>

            <p className="text-sm text-gray-500">
                {value}
            </p>
        </div>
    );
}