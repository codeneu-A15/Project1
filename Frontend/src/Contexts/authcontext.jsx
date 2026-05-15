/* eslint-disable react-refresh/only-export-components */
import React from "react"
import Loading from "../Component/Loading"
import onAuthStateChange from "../../../Backend/"
const authContext = React.createContext()
export default function AuthProvider({children}) {
    const [loading, setLoading] = React.useState(true)
    const [userLoggedIn, setUserLoggedIn] = React.useState(false)
    const [currentUser, setCurrentUser] = React.useState(null)
    const [authError, setAuthError] = React.useState("")
    function HandleUser(user) {
        setAuthError("")
        if (user) {
            setUserLoggedIn(true)
            setCurrentUser({...user})
        } else {
            setUserLoggedIn(false)
            setCurrentUser(null)
        }
        setLoading(authError)
    }
    function handleServerAuthError(error) {
        setLoading(false)
        setCurrentUser(null)
        setUserLoggedIn(false)
        setAuthError(error)
    } 
    React.useState(() => {
        const authListener = onAuthStateChange(handleServerAuthError, HandleUser)
        return authListener
    }, [])
    const value = {loading, userLoggedIn, currentUser, authError} 
    return (
        <AuthProvider.Provider value={value} >
            {(!loading) ? children: <Loading />}
        </AuthProvider.Provider>
    )
}
export function useAuth() {
    return React.useContext(authContext)
}