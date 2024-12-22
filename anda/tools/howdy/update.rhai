rpm.global("commit", gh_commit("boltgolt/howdy"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}