/* eslint-disable no-unused-vars */
import {Outlet, Navigate} from "react-router"
import { useAuth } from "../../Contexts/authcontext"
export function ProtectedRoute({type}) {
    const {userLoggedIn} = useAuth()
    if (userLoggedIn) {
        <Outlet />
    } else {
        <Navigate to="/Signup" />
    }
}