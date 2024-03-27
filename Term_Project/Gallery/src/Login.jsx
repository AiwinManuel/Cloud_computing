import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styled from "styled-components";
import Button from "./components/Button"; 
import Input from "./components/Input";
import './LoginStyle.css';



function Login() {
  let navigate = useNavigate();

  // State for email and password
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // Hardcoded credentials for demonstration
  const correctEmail = "aiwin@aiwin.com";
  const correctPassword = "aiwin";

  const handleLogin = () => {
    console.log(email,password);
    // Simple credential check
    if (email === correctEmail && password === correctPassword) {
      navigate('/gallery');
    } else {
      alert('Incorrect credentials');
    }
  };

  return (
    <MainContainer>
      <WelcomeText>Welcome</WelcomeText>
      <InputContainer>
        <Input type="text" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <Input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </InputContainer>
      <ButtonContainer>
        <Button content="Log In" onClick={handleLogin} />
      </ButtonContainer>
    </MainContainer>
  );
}


const MainContainer = styled.div`
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  margin:220px;
  height: fit-content;
  width: 50vw;
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(8.5px);
  -webkit-backdrop-filter: blur(8.5px);
  border-radius: 10px;
  color: #ffffff;
  text-transform: uppercase;
  letter-spacing: 0.4rem;
  
`;

const WelcomeText = styled.h2`
  margin: 3rem 0 2rem 0;
`;

const InputContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height: 20%;
  width: 100%;
`;

const ButtonContainer = styled.div`
  margin: 1rem 0 2rem 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
`;


export default Login;