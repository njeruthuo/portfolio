document
  .getElementById("whatsappButton")
  .addEventListener("click", function () {
    var whatsappNumber = "+254768585724";
    var message = "Hello! I'm contacting you from your portfolio website.";
    var whatsappURL =
      "https://wa.me/" +
      whatsappNumber +
      "?text=" +
      encodeURIComponent(message);
    window.location.href = whatsappURL;
  });
