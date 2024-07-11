#!/usr/bin/env puppet

# Install Nginx if it's not already installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Holberton School',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Update the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('web_static/default.conf.erb'),
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
#!/usr/bin/env puppet

# Install Nginx if it's not already installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Holberton School',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Update the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('web_static/default.conf.erb'),
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
}}
