g_systbl = {

  0 : [ 2,					"io_setup"		],
  1 : [ 1,					"io_destroy"		],
  2 : [ 3,					"io_submit"		],
  3 : [ 3,					"io_cancel"		],
  4 : [ 5,			  	"io_getevents"		],
  5 : [ 5,					"setxattr"		],
  6 : [ 5,					"lsetxattr"		],
  7 : [ 5,					"fsetxattr"		],
  8 : [ 4,					"getxattr"		],
  9 : [ 4,					"lgetxattr"		],
 10 : [ 4,					"fgetxattr"		],
 11 : [ 3,					"listxattr"		],
 12 : [ 3,					"llistxattr"		],
 13 : [ 3,					"flistxattr"		],
 14 : [ 2,					"removexattr"		],
 15 : [ 2,					"lremovexattr"		],
 16 : [ 2,					"fremovexattr"		],
 17 : [ 2,				  "getcwd"		],
 18 : [ 3,					"lookup_dcookie"	],
 19 : [ 2,					"eventfd2"		],
 20 : [ 1,					"epoll_create1"		],
 21 : [ 4,					"epoll_ctl"		],
 22 : [ 6,					"epoll_pwait"		],
 23 : [ 1,			"dup"			],
 24 : [ 3,			"dup3"			],
 25 : [ 3,			"fcntl"			],
 26 : [ 1,					"inotify_init1"		],
 27 : [ 3,					"inotify_add_watch"	],
 28 : [ 2,					"inotify_rm_watch"	],
 29 : [ 3,			"ioctl"			],
 30 : [ 3,					"ioprio_set"		],
 31 : [ 2,					"ioprio_get"		],
 32 : [ 2,				"flock"			],
 33 : [ 4,				"mknodat"		, 0x2],
 34 : [ 3,				"mkdirat"		, 0x2],
 35 : [ 3,				"unlinkat"	, 0x2],
 36 : [ 3,				"symlinkat"	, 0x2|(1<<3)],
 37 : [ 5,				"linkat"		, 0x2|(1<<3)],
 38 : [ 4,				"renameat"		, 0x2|(1<<3)],
 39 : [ 2,				"umount2"		],
 40 : [ 5,				"mount"			],
 41 : [ 2,				"pivot_root"		],
 42 : [ 3,			"nfsservctl"		],
 43 : [ 2,				"statfs"		, 0x1],
 44 : [ 2,				"fstatfs"		],
 45 : [ 2,				"truncate"		,0x1],
 46 : [ 2,				"ftruncate"		],
 47 : [ 4,				"fallocate"		],
 48 : [ 3,				"faccessat"		,0x2],
 49 : [ 1,				"chdir"			,0x1],
 50 : [ 1,				"fchdir"		],
 51 : [ 1,				"chroot"		],
 52 : [ 2,				"fchmod"		],
 53 : [ 3,				"fchmodat"		, 0x2],
 54 : [ 5,				"fchownat"		, 0x2],
 55 : [ 3,				"fchown"		],
 56 : [ 4,				"openat"		, 0x2],
 57 : [ 1,				"close"			],
 58 : [ 0,				"vhangup"		],
 59 : [ 2,				"pipe2"			],
 60 : [ 4,				"quotactl"		],
 61 : [ 3,			"getdents64"		],
 62 : [ 3,				"lseek"			],
 63 : [ 3,				"read"			],
 64 : [ 3,				"write"			],
 65 : [ 3,				"readv"			],
 66 : [ 3,				"writev"		],
 67 : [ 4,				"pread64"		],
 68 : [ 4,				"pwrite64"		],
 69 : [ 4,				"preadv"		],
 70 : [ 4,				"pwritev"		],
 71 : [ 4,			"sendfile"		],
 72 : [ 6,			"pselect6"		],
 73 : [ 5,			"ppoll"			],
 74 : [ 4,				"signalfd4"		],
 75 : [ 4,				"vmsplice"		],
 76 : [ 6,				"splice"		],
 77 : [ 4,				"tee"			],
 78 : [ 4,			"readlinkat"		, 0x2],
 79 : [ 4,			"newfstatat"		, 0x2],
 80 : [ 2,				"fstat"			],
 81 : [ 0,				"sync"			],
 82 : [ 1,				"fsync"			],
 83 : [ 1,				"fdatasync"		],
 84 : [ 4,			"sync_file_range"	],
 85 : [ 2,			"timerfd_create"	],
 86 : [ 4,			"timerfd_settime"	],
 87 : [ 2,			"timerfd_gettime"	],
 88 : [ 4,			"utimensat"		],
 89 : [ 1,				"acct"			],
 90 : [ 2,				"capget"		],
 91 : [ 2,				"capset"		],
 92 : [ 1,			"personality"		],
 93 : [ 1,				"exit"			],
 94 : [ 1,				"exit_group"		],
 95 : [ 5,				"waitid"		],
 96 : [ 1,			"set_tid_address"	],
 97 : [ 1,				"unshare"		],
 98 : [ 6,			"futex"			],
 99 : [ 2,			"set_robust_list"	],
100 : [ 3,			"get_robust_list"	],
101 : [ 2,			"nanosleep"		],
102 : [ 2,				"getitimer"		],
103 : [ 3,				"setitimer"		],
104 : [ 4,			"kexec_load"		],
105 : [ 3,			"init_module"		],
106 : [ 2,			"delete_module"		],
107 : [ 3,			"timer_create"		],
108 : [ 2,			"timer_gettime"		],
109 : [ 1,			"timer_getoverrun"	],
110 : [ 4,			"timer_settime"		],
111 : [ 1,			"timer_delete"		],
112 : [ 2,			"clock_settime"		],
113 : [ 2,			"clock_gettime"		],
114 : [ 2,		"clock_getres"		],
115 : [ 4,		"clock_nanosleep"	],
116 : [ 3,				"syslog"		],
117 : [ 4,				"ptrace"		],
118 : [ 2,			"sched_setparam"	],
119 : [ 3,		"sched_setscheduler"	],
120 : [ 1,		"sched_getscheduler"	],
121 : [ 2,			"sched_getparam"	],
122 : [ 3,			"sched_setaffinity"	],
123 : [ 3,			"sched_getaffinity"	],
124 : [ 0,			"sched_yield"		],
125 : [ 1,		"sched_get_priority_max"],
126 : [ 1,		"sched_get_priority_min"],
127 : [ 2,	"sched_rr_get_interval"],
128 : [ 0,			"restart_syscall"	],
129 : [ 2,				"kill"			],
130 : [ 2,				"tkill"			],
131 : [ 3,				"tgkill"		],
132 : [ 2,			"sigaltstack"		],
133 : [ 2,			"rt_sigsuspend"		],
134 : [ 4,			"rt_sigaction"		],
135 : [ 4,			"rt_sigprocmask"	],
136 : [ 2,			"rt_sigpending"		],
137 : [ 4,		"rt_sigtimedwait"	],
138 : [ 3,			"rt_sigqueueinfo"	],
139 : [ 0,			"rt_sigreturn"		],
140 : [ 3,			"setpriority"		],
141 : [ 2,			"getpriority"		],
142 : [ 4,				"reboot"		],
143 : [ 2,				"setregid"		],
144 : [ 1,				"setgid"		],
145 : [ 2,				"setreuid"		],
146 : [ 1,				"setuid"		],
147 : [ 3,				"setresuid"		],
148 : [ 3,				"getresuid"		],
149 : [ 3,				"setresgid"		],
150 : [ 3,				"getresgid"		],
151 : [ 1,				"setfsuid"		],
152 : [ 1,				"setfsgid"		],
153 : [ 1,				"times"			],
154 : [ 2,				"setpgid"		],
155 : [ 1,				"getpgid"		],
156 : [ 1,				"getsid"		],
157 : [ 0,				"setsid"		],
158 : [ 2,				"getgroups"		],
159 : [ 2,				"setgroups"		],
160 : [ 1,				"uname"			],
161 : [ 2,			"sethostname"		],
162 : [ 2,			"setdomainname"		],
163 : [ 2,				"getrlimit"		],
164 : [ 2,				"setrlimit"		],
165 : [ 2,				"getrusage"		],
166 : [ 1,				"umask"			],
167 : [ 5,				"prctl"			],
168 : [ 3,				"getcpu"		],
169 : [ 2,			"gettimeofday"		],
170 : [ 2,			"settimeofday"		],
171 : [ 1,			"adjtimex"		],
172 : [ 0,				"getpid"		],
173 : [ 0,				"getppid"		],
174 : [ 0,			"getuid"		],
175 : [ 0,				"geteuid"		],
176 : [ 0,			"getgid"		],
177 : [ 0,				"getegid"		],
178 : [ 0,				"gettid"		],
179 : [ 1,				"sysinfo"		],
180 : [ 4,				"mq_open"		],
181 : [ 1,				"mq_unlink"		],
182 : [ 5,		"mq_timedsend"		],
183 : [ 5,		"mq_timedreceive"	],
184 : [ 2,				"mq_notify"		],
185 : [ 3,			"mq_getsetattr"		],
186 : [ 2,				"msgget"		],
187 : [ 3,				"msgctl"		],
188 : [ 5,				"msgrcv"		],
189 : [ 4,				"msgsnd"		],
190 : [ 3,				"semget"		],
191 : [ 4,				"semctl"		],
192 : [ 4,			"semtimedop"		],
193 : [ 3,				"semop"			],
194 : [ 3,				"shmget"		],
195 : [ 3,				"shmctl"		],
196 : [ 3,				"shmat"			],
197 : [ 1,				"shmdt"			],
198 : [ 3,				"socket"		],
199 : [ 4,			"socketpair"		],
200 : [ 3,				"bind"			],
201 : [ 2,				"listen"		],
202 : [ 3,				"accept"		],
203 : [ 3,				"connect"		],
204 : [ 3,			"getsockname"		],
205 : [ 3,			"getpeername"		],
206 : [ 6,				"sendto"		],
207 : [ 6,				"recvfrom"		],
208 : [ 5,			"setsockopt"		],
209 : [ 5,			"getsockopt"		],
210 : [ 2,				"shutdown"		],
211 : [ 3,				"sendmsg"		],
212 : [ 3,				"recvmsg"		],
213 : [ 3,				"readahead"		],
214 : [ 1,				"brk"			],
215 : [ 2,				"munmap"		],
216 : [ 5,				"mremap"		],
217 : [ 5,				"add_key"		],
218 : [ 4,			"request_key"		],
219 : [ 5,				"keyctl"		],
220 : [ 5,				"clone"			],
221 : [ 3,				"execve"		, 0x1],
222 : [ 6,				"mmap"			],
223 : [ 4,				"fadvise64"		],
224 : [ 2,				"swapon"		],
225 : [ 1,				"swapoff"		],
226 : [ 3,				"mprotect"		],
227 : [ 3,				"msync"			],
228 : [ 2,				"mlock"			],
229 : [ 2,				"munlock"		],
230 : [ 1,				"mlockall"		],
231 : [ 0,			"munlockall"		],
232 : [ 3,				"mincore"		],
233 : [ 3,				"madvise"		],
234 : [ 5,			"remap_file_pages"	],
235 : [ 6,				"mbind"			],
236 : [ 5,			"get_mempolicy"		],
237 : [ 3,			"set_mempolicy"		],
238 : [ 4,			"migrate_pages"		],
239 : [ 6,			"move_pages"		],
240 : [ 4,			"rt_tgsigqueueinfo"	],
241 : [ 5,			"perf_event_open"	],
242 : [ 4,				"accept4"		],
243 : [ 5,			"recvmmsg"		],

260 : [ 4,				"wait4"			],
261 : [ 4,				"prlimit64"		],
262 : [ 2,			"fanotify_init"		],
263 : [ 5,			"fanotify_mark"		],
264 : [ 5,			"name_to_handle_at"	],
265 : [ 3,			"open_by_handle_at"	],
266 : [ 2,			"clock_adjtime"		],
267 : [ 1,				"syncfs"		],
268 : [ 2,				"setns"			],
269 : [ 4,				"sendmmsg"		],
270 : [ 6,			"process_vm_readv"	],
271 : [ 6,			"process_vm_writev"	],
272 : [ 5,				"kcmp"			],
273 : [ 3,			"finit_module"		],
274 : [ 3,			"sched_setattr"		],
275 : [ 4,			"sched_getattr"		],
276 : [ 5,				"renameat2"		, 0x2|(1<<3)],
277 : [ 3,				"seccomp"		],
278 : [ 3,				"getrandom"		],
279 : [ 2,			"memfd_create"		],
280 : [ 3,				"bpf"			],
281 : [ 5,				"execveat"		, 0x2],
282 : [ 1,			"userfaultfd"		],
283 : [ 3,			"membarrier"		],
284 : [ 3,				"mlock2"		],
285 : [ 6,			"copy_file_range"	],
286 : [ 6,				"preadv2"		],
287 : [ 6,				"pwritev2"		],
288 : [ 4,			"pkey_mprotect"		],
289 : [ 2,			"pkey_alloc"		],
290 : [ 1,				"pkey_free"		],
291 : [ 5,				"statx"			],
292 : [ 6,		"io_pgetevents"		],
293 : [ 4,				"rseq"			],
294 : [ 5,			"kexec_file_load"	],
#/* 295 ... 423 - reserved to sync up with other architectures */

}

#print(g_systbl)