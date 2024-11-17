$(document).ready(function () {
  var today = new Date();

  var maxDate = new Date(today);
  maxDate.setFullYear(today.getFullYear() + 1);

  $("#date-picker").datepicker({
    minDate: 0,
    maxDate: maxDate,
  });
});
