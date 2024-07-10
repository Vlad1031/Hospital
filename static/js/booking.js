document.addEventListener('DOMContentLoaded', function () {
    var dateTimeInput = document.getElementById('appointmentDate');
    dateTimeInput.addEventListener('change', function () {
        var value = this.value;
        var [date, time] = value.split('T');
        var [year, month, day] = date.split('-');
        var formattedDate = `${day}-${month}-${year}`;
        this.value = `${year}-${month}-${day}T${time}`;
    });

    var phoneInput = document.getElementById('phone');
    phoneInput.addEventListener('focus', function () {
        if (this.value === '') {
            this.value = '+380';
        }
    });
    phoneInput.addEventListener('blur', function () {
        if (this.value === '+380') {
            this.value = '';
        }
    });
});

document.getElementById('age').addEventListener('input', function (event) {
    if (event.target.value < 0) {
        event.target.value = 0;
    }
});