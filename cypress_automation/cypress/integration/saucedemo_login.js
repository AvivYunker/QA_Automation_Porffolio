describe('SauceDemo Login Functionality', () => {
  it('should allow a user to login with valid credentials', () => {
    // Visit the SauceDemo login page
    cy.visit('https://www.saucedemo.com/');

    // Wait for the username input to be visible
    cy.get('input[placeholder="Username"]').should('be.visible');

    // Get username and password elements
    const usernameInput = cy.get('input[placeholder="Username"]');
    const passwordInput = cy.get('input[placeholder="Password"]');
    const loginButton = cy.get('input[id="login-button"]');

    // Enter username and password
    usernameInput.type('standard_user');
    passwordInput.type('secret_sauce');

    // Click the login button
    loginButton.click();

    // Validate that the login was successful
    cy.url().should('include', '/inventory.html');
    cy.get('.inventory_list').should('be.visible');
  });
});

// npx cypress run --spec "cypress/integration/saucedemo_login.js"