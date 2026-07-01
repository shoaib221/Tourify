import React, { useContext, useState } from 'react';

import { AuthContext } from './context';
import { FaGithub } from "react-icons/fa";
import { toast } from 'react-toastify';





export const GithubLogin = () => {
    const { user, setUser } = useContext(AuthContext)

    function SignIn() {
        signInWithPopup(auth, provider)
            .then((result) => {
                // This gives you a GitHub Access Token. You can use it to access the GitHub API.
                // const credential = GithubAuthProvider.credentialFromResult(result);
                // const token = credential.accessToken;


                const user = result.user;
                //console.log( user.email )
                setUser(user);

            }).catch((error) => {
                // Handle Errors here.
                toast.error(error.message)

                // The email of the user's account used.
                // const email = error.customData.email;
                // The AuthCredential type that was used.
                //const credential = GithubAuthProvider.credentialFromError(error);
                // ...
            });
    }


    return (
        <button className='button-1 w-full cen-hor gap-4' style={{ cursor: 'initial' }} >
            <FaGithub />
            Enter With Github
        </button>
    )

};

