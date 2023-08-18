import React, { useContext } from "react";
import { Context } from "./Layout";

import { Navbar, Container, Image, NavDropdown, Nav } from "react-bootstrap";
import { Link } from "react-router-dom";
import { getUser, useUserActions } from "../hooks/user.actions";

function NavigationBar() {
  const { setToaster } = useContext(Context);

  const userActions = useUserActions();

  const user = getUser();

  const handleLogout = () => {
    userActions.logout().catch((e) =>
      setToaster({
        type: "danger",
        message: "Выход не получился",
        show: true,
        title: e.data?.detail | "Ошибка.",
      })
    );
  };

  return (
    <Navbar bg="primary" variant="dark">
      <Container>
        <Navbar.Brand className="fw-bold" as={Link} to={`/`}>
          Postagram
        </Navbar.Brand>
        <Navbar.Collapse className="justify-content-end">
          <Nav>
            <NavDropdown
              title={
                <Image src={user.avatar} roundedCircle width={36} height={36} />
              }
            >
              <NavDropdown.Item as={Link} to={`/profile/${user.id}/`}>
                Аккаунт
              </NavDropdown.Item>
              <NavDropdown.Item onClick={handleLogout}>Выйти</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavigationBar;
