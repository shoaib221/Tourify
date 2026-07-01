import React, { useContext, useState } from 'react';
import { AuthContext, useAuthContext } from './context';
import { ImGoogle2 } from "react-icons/im";
import { toast } from 'react-toastify';
import { GoogleLogin } from "@react-oauth/google";
import axios from 'axios';
import { backendURL } from './context';

const Call = axios.create({
    baseURL: backendURL
})


export const LoginGoogle = () => {
    const {  Login } = useAuthContext();

    async function fetchJwtToken(credentialResponse) {
        try {
            //console.log( credentialResponse.credential );
            let res = await Call.post('/accounts/google-login/',
                {
                    token: credentialResponse.credential
                },
                {
                    headers: {
                        "Content-Type": "application/json"
                    }
                }
            )

            if( res.data.user ) Login( res.data.user )
        } catch (err) {
            console.error(err);
        }

    }

    return <GoogleLogin onSuccess={fetchJwtToken} />;

}

