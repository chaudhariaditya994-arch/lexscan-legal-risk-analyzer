import PropTypes from "prop-types";

export default function UploadView({ onFileSelect, disabled }) {
  function handleChange(event) {
    const file = event.target.files?.[0];
    if (file) {
      onFileSelect(file);
    }
  }

  function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files?.[0];
    if (file) {
      onFileSelect(file);
    }
  }

  return (
    <section
      onDragOver={(event) => event.preventDefault()}
      onDrop={handleDrop}
      style={{
        border: "2px dashed #94a3b8",
        borderRadius: 24,
        padding: 40,
        textAlign: "center",
        background: "rgba(255,255,255,0.9)",
      }}
    >
      <h2 style={{ marginTop: 0 }}>Upload a legal document</h2>
      <p>Drop a PDF here or browse for a contract, lease, NDA, or offer letter.</p>
      <input type="file" accept="application/pdf" onChange={handleChange} disabled={disabled} />
    </section>
  );
}

UploadView.propTypes = {
  onFileSelect: PropTypes.func.isRequired,
  disabled: PropTypes.bool,
};

UploadView.defaultProps = {
  disabled: false,
};
