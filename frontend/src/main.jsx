import { createRoot } from 'react-dom/client';
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import 'react-toastify/dist/ReactToastify.css';
import { useState } from 'react';
import { ToastContainer } from 'react-toastify';
import { BrowserRouter, Routes, Route, Outlet } from 'react-router-dom';
import { NotFound } from './lib/miscel/NotFound.jsx';
import { GoogleOAuthProvider } from "@react-oauth/google";
import './lib/Box/box1.css';
import './index.css';
import "./lib/Buttons/button.css";
import './lib/Theme/Theme.css'
import { Entry } from './routes/Entry.jsx';
import { Home } from './routes/Home.jsx';
import { Auth } from './lib/auth/auth.jsx';
import { AuthProvider } from './lib/auth/context.jsx';
import { Profile } from './routes/profile/profile.jsx';



const queryClient = new QueryClient();

const App = () => {
    let google_client_id = import.meta.env.VITE_GOOGLE_CLIENT

    return (
        <BrowserRouter>
            <GoogleOAuthProvider clientId={google_client_id} >
                <AuthProvider>
                    <QueryClientProvider client={queryClient} >

                        <ToastContainer />
                        <Routes>
                            <Route path='/' element={<Entry />} >
                                <Route index element={<Home />} />
                                <Route path='auth' element={< Auth />} />
                                <Route path='profile/' element={ <Profile /> } >
                                    {/* <Route path='about' element={} />
                                    <Route path='past_trip' element={} />
                                    <Route path='connection' element={} /> */}
                                </Route>
                                <Route path="*" element={<NotFound />} />
                            </Route>
                        </Routes>

                    </QueryClientProvider>
                </AuthProvider>
            </GoogleOAuthProvider>
        </BrowserRouter>
    )
}



createRoot(document.getElementById('root')).render(<App />);

