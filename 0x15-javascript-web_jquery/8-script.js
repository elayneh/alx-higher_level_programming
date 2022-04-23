$(document).ready(function () {
  const salutUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $helloElement = $('div#hello');

  function getSalut () {
    return $.get({
      url: salutUrl,
      dataType: 'json'
    });
  }

  getSalut().then((res) => {
    $helloElement.text(res.hello);
  });
});
