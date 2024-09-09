import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import JobPostingForm from '../components/JobPostingForm';
import JobListingManager from '../components/JobListingManager';

const EmployerDashboard = () => {
    return (
        <div style={{ fontFamily: '"Roboto", sans-serif', backgroundColor: '#F5F5F5', padding: '16px' }}>
            <Header />
            <div style={{ maxWidth: '80%', margin: '0 auto', padding: '16px', backgroundColor: '#FFFFFF', borderRadius: '4px', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)' }}>
                <h1 style={{ color: '#212121', fontSize: '24px', fontWeight: '700', lineHeight: '1.5', marginBottom: '16px' }}>Employer Dashboard</h1>
                <p style={{ color: '#757575', fontSize: '14px', lineHeight: '1.6', marginBottom: '24px' }}>The EmployerDashboard serves as a comprehensive interface for employers, featuring the Header, Footer, an innovative JobPostingForm, and a JobListingManager to streamline job posting and management processes.</p>
                <JobPostingForm />
                <JobListingManager />
            </div>
            <Footer />
        </div>
    );
};

export default EmployerDashboard;