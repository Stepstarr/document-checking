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
                            <input class="input is-medium is-rounded" type="email" placeholder="设置账号" autocomplete="username" required />
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input class="input is-medium is-rounded" type="password" placeholder="设置密码" autocomplete="current-password" required />
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input class="input is-medium is-rounded" type="password" placeholder="确认密码" autocomplete="current-password" required />
                        </div>
                    </div>
                    <br />
                    <button class="button is-block is-fullwidth is-primary is-medium is-rounded" type="submit">
                        注册
                    </button>
                </form>
                <br>
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <a href="#">返回登陆界面</a>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <a href="#">管理员注册</a>
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
  name: 'Home',
  data () {
    return {
        account: '',
        password: '',
        confirmPassword: '',
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