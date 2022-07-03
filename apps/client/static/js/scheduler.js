
Vue.component('scheduler')

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#scheduler',
    data: {
        days_week: [],
        hours_week: [],
        description: '',
        edit: false,
        active: true,
        selected_day: '',
        selected_hour: '',
        nome: '',
        email: '',
        telefone: '',
    },
    mounted() {
        axios.get('scheduler_api/days_weeks/').then(response => {
            this.days_week = response.data
        })

    },
    methods: {
        changeWeek: function () {
            this.hours_week = []
            this.selected_hour = ''
            axios.get('scheduler_api/hours_day/' + this.selected_day).then(response => {
                this.hours_week = response.data
            }).catch(
                function (error) {
                    console.log(error)
                }
            )
        },

        saveScheduler: function () {
            let data = {
                "name": this.nome,
                "email": this.email,
                "cellphone": this.telefone,
                "days_week": this.selected_day,
                "hours_days": this.selected_hour
            };

            axios.post('scheduler_api/scheduler/', data).then(
                response => {
                    Swal.fire({
                        title: 'Deu tudo certo com sua escolha',
                        text: `A Sua escolha foi this. ${response.data.nome_day} às ${response.data.nome_hora}`,
                        icon: 'success',
                        confirmButtonText: 'Cool'
                    }).then((result) => {
                        window.location.reload();
                      })

                }

            ).catch(
                function (error) {
                    console.log(error.response.data)
                    Swal.fire({
                        title: 'Aconteceu um error',
                        text: JSON.stringify(error.response.data),
                        icon: 'error',
                        confirmButtonText: 'fechar'
                    }).then((result) => {
                        window.location.reload();
                      })
                }
            )
        }
    }
})