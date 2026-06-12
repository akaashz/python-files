
USE moviebookingsystem;

-- USERS TABLE
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- MOVIES TABLE
CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(100) NOT NULL,
    language VARCHAR(50)
);

-- THEATRES TABLE
CREATE TABLE theatres (
    theatre_id INT AUTO_INCREMENT PRIMARY KEY,
    theatre_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- SHOWS TABLE
CREATE TABLE shows (
    show_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    theatre_id INT,
    show_date DATE,
    show_time TIME,
    ticket_price DECIMAL(10,2),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (theatre_id) REFERENCES theatres(theatre_id)
);

-- BOOKINGS TABLE
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    show_id INT NULL,
    booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    seats INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (show_id) REFERENCES shows(show_id)
);

-- PAYMENTS TABLE
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    payment_method VARCHAR(50),
    payment_status VARCHAR(20),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- THEATRE SELECTION TABLE
CREATE TABLE theatre_selection (
    id INT AUTO_INCREMENT PRIMARY KEY,
    theatre_name VARCHAR(100),
    location VARCHAR(200),
    show_time VARCHAR(20)
);