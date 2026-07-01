
import React, { createContext, useContext, useEffect, useState, useRef } from "react";
import { toast } from "react-toastify";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export const AuthContext = createContext();
export const useAuthContext = () => useContext(AuthContext);

const baseURL = "http://localhost:8000/api";
// const baseURL = "https://express-practice-chi.vercel.app/";

export const backendURL = baseURL;

const axiosInstance = axios.create({
    baseURL,
    headers: { "Content-Type": "application/json" },
});


export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    

    
    const LogOut = () => {
        setUser(null);
        localStorage.removeItem( 'accessToken' )
        localStorage.removeItem( 'refreshToken' )
    };

    
    const Login = (user) => {
        setUser( user )
        localStorage.setItem( 'accessToken', user[ 'accessToken' ] )
        localStorage.setItem( 'refreshToken', user[ 'refreshToken' ] )
    }

    

    const value = {
        user,
        loading,
        LogOut,
        axiosInstance,
        Login,
        setUser
    };

    return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
