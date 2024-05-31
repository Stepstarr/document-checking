<template>
    <div>
        <nav class="navbar is-dark " role="navigation" aria-label="main navigation">
            <div class="container">
                <div class="navbar-brand">
                    <router-link class="navbar-item is-size-4 has-text-weight-bold ml-4" :to="'/'">
                        Docx Format Checker
                    </router-link>
                    <span class="navbar-burger burger" data-target="navbarMenu">
                        <span></span>
                        <span></span>
                        <span></span>
                    </span>
                </div>
                <div id="navbarMenu" class="navbar-menu">
                    <div class="navbar-end">
                        <div class="navbar-item has-dropdown is-hoverable">
                            <a class="navbar-link">账号</a>
                            <div class="navbar-dropdown">
                                <a class="navbar-item">模板管理</a>
                                <a class="navbar-item">设置</a>
                                <hr class="navbar-divider">
                                <div class="navbar-item">退出登录</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
</script>