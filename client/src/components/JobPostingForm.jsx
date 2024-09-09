import React, { useState } from 'react';

const JobPostingForm = (props) => {
  const [jobTitle, setJobTitle] = useState('');
  const [description, setDescription] = useState('');
  const [requirements, setRequirements] = useState('');
  const [location, setLocation] = useState('');
  const [jobType, setJobType] = useState('');
  const [deadline, setDeadline] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const jobListing = {
      jobTitle,
      description,
      requirements,
      location,
      jobType,
      deadline,
    };
    // Logic to send jobListing to the parent or API
    props.onSubmit(jobListing);
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-lg mx-auto p-6 bg-white shadow-md rounded-lg">
      <h2 className="text-2xl font-bold text-heading mb-4">Create Job Listing</h2>
      <div className="mb-4">
        <label className="block text-sm font-medium text-heading mb-1">Job Title</label>
        <input
          type="text"
          value={jobTitle}
          onChange={(e) => setJobTitle(e.target.value)}
          className="border border-borderColors p-2 w-full rounded focus:outline-none focus:border-primaryColor"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium text-heading mb-1">Description</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="border border-borderColors p-2 w-full rounded focus:outline-none focus:border-primaryColor"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium text-heading mb-1">Requirements</label>
        <textarea
          value={requirements}
          onChange={(e) => setRequirements(e.target.value)}
          className="border border-borderColors p-2 w-full rounded focus:outline-none focus:border-primaryColor"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium text-heading mb-1">Location</label>
        <input
          type="text"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          className="border border-borderColors p-2 w-full rounded focus:outline-none focus:border-primaryColor"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium text-heading mb-1">Job Type</label>
        <input
          type="text"
          value={jobType}
          onChange={(e) => setJobType(e.target.value)}
          className="border border-borderColors p-2 w-full rounded focus:outline-none focus:border-primaryColor"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium text-heading mb-1">Application Deadline</label>
        <input
          type="date"
          value={deadline}
          onChange={(e) => setDeadline(e.target.value)}
          className="border border-borderColors p-2 w-full rounded focus:outline-none focus:border-primaryColor"
          required
        />
      </div>
      <button
        type="submit"
        className="bg-primaryButton text-white font-semibold py-2 px-4 rounded transition duration-300 ease-in-out hover:bg-opacity-80"
      >
        Submit Job Listing
      </button>
    </form>
  );
};

export default JobPostingForm;