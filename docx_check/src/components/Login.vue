<template>
    <div class="container">
        <section class="hero is-fullheight">
            <div class="hero-body has-text-centered is-flex is-justify-content-center is-align-items-center">
                <div class="login">
                <h1 class="title">文档格式自动化检测系统</h1>
                <br />
                <form>
                    <div class="field">
                    <div class="control">
                        <input class="input is-medium is-rounded" type="email" placeholder="账号" autocomplete="username" required />
                    </div>
                    </div>
                    <div class="field">
                    <div class="control">
                        <input class="input is-medium is-rounded" type="password" placeholder="密码" autocomplete="current-password" required />
                    </div>
                    </div>
                    <br />
                    <button class="button is-block is-fullwidth is-primary is-medium is-rounded" type="submit">
                        登录
                    </button>
                </form>
                <br>
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <a href="#">忘记密码?</a>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <a href="#">创建新账号</a>
                        </div>
                    </div>
                </nav>
                </div>
            </div>
        </section>
    </div>
    
</template>
<script>
export default {
    name: 'Login',
    data () {
      return {
        account: '',
        password: '',
      }
    },
    computed: {

    },
    watch: {

    },
    methods: {

    },
}
</script>