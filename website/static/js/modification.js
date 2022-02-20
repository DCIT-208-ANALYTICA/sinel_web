const menuToggler = document.querySelector("#menu-toggler")
const body = document.querySelector("body")
const drawer = document.querySelector("#nav-drawer")
const overlay = document.querySelector(".overlay")
const content = document.querySelector(".content")

menuToggler?.addEventListener("click", (event) => {
	toggleSideDrawer()
})

overlay?.addEventListener("click", (event) => {
	toggleSideDrawer()
})

function toggleSideDrawer() {
	body?.classList.toggle("no-scroll")
	drawer?.classList.toggle("active")
	overlay?.classList.toggle("active")
	content?.classList.toggle("active")
}